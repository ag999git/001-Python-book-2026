
#!/usr/bin/env python3
"""
Generate awesome-pages `.pages` files for the MkDocs site from SUMMARY.md.

SUMMARY.md is GitBook's navigation file. MkDocs cannot read it, so this script
translates it into the `.pages` files that the mkdocs-awesome-pages-plugin uses,
making SUMMARY.md the single source of navigation for both sites.

Usage:  gen_mkdocs_pages.py <summary.md> <docs-dir>

Safety: this script never raises. If anything is wrong it reports the problem,
writes nothing for the affected folder, and exits 0. A folder with no `.pages`
file simply falls back to the plugin's automatic navigation, which is exactly
how the site behaves today.
"""
import os, re, sys

ENTRY = re.compile(r'^\*\s*\[(.+?)\]\((.+?)\)\s*$')
HEAD  = re.compile(r'^##\s+(.*\S)\s*$')


def yq(s):
    """Quote a YAML scalar safely, stripping markdown that a nav label cannot render."""
    s = str(s).replace('`', '')          # MkDocs nav shows backticks literally
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def parse_summary(path):
    """-> (sections, colab) where sections is [(title, [(label, folder, file)])]"""
    sections, colab, cur = [], [], None
    with open(path, encoding='utf-8') as fh:
        for raw in fh:
            line = raw.rstrip('\n')
            m = HEAD.match(line)
            if m:
                cur = (m.group(1), [])
                sections.append(cur)
                continue
            m = ENTRY.match(line.strip())
            if not m or cur is None:
                continue
            label, target = m.group(1).strip(), m.group(2).strip()
            if target.startswith(('http://', 'https://')):
                nb = target.rstrip('/').split('/')[-1]
                if nb.endswith('.ipynb'):
                    colab.append((label, nb))
                continue
            target = target.split('#')[0]
            if '/' not in target:
                continue
            folder, _, fname = target.partition('/')
            cur[1].append((label, folder, fname))
    return sections, colab


def write_pages(path, title, entries):
    lines = []
    if title:
        lines.append('title: %s' % yq(title))
    lines.append('nav:')
    for label, fname in entries:
        lines.append('  - %s: %s' % (yq(label), fname))
    # SAFETY: "..." means "then everything else". Without it, any page missing
    # from this list would vanish from the site navigation. With it, a partial
    # or failed generation can only ever mis-ORDER pages, never hide them.
    lines.append('  - ...')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines) + '\n')


def main():
    if len(sys.argv) != 3:
        print('usage: gen_mkdocs_pages.py <summary.md> <docs-dir>')
        return 0
    summary, docs = sys.argv[1], sys.argv[2]
    if not os.path.isfile(summary):
        print('SKIP: no SUMMARY.md at %s - leaving navigation automatic' % summary)
        return 0
    if not os.path.isdir(docs):
        print('SKIP: no docs dir at %s' % docs)
        return 0

    sections, colab = parse_summary(summary)
    order, written, skipped = [], 0, 0

    for title, items in sections:
        # group this section's entries by folder, preserving SUMMARY order
        by_folder = {}
        for label, folder, fname in items:
            by_folder.setdefault(folder, []).append((label, fname))
        for folder, entries in by_folder.items():
            if folder == 'colab-nb':
                continue          # handled separately below (notebooks, not pages)
            fdir = os.path.join(docs, folder)
            if not os.path.isdir(fdir):
                print('SKIP folder (not in docs): %s' % folder); skipped += 1; continue
            resolved = []
            for label, fname in entries:
                # the sync renames every README.md to index.md
                cand = 'index.md' if fname.lower() == 'readme.md' else fname
                if os.path.isfile(os.path.join(fdir, cand)):
                    resolved.append((label, cand))
                else:
                    print('  drop (file absent): %s/%s' % (folder, cand))
            if not resolved:
                print('SKIP %s: no resolvable entries' % folder); skipped += 1; continue
            write_pages(os.path.join(fdir, '.pages'), title, resolved)
            print('wrote %s/.pages  (%d entries)' % (folder, len(resolved)))
            written += 1
            if folder not in order:
                order.append(folder)

    # --- colab-nb: MkDocs renders notebooks in place, so list the local files ---
    cdir = os.path.join(docs, 'colab-nb')
    if os.path.isdir(cdir):
        entries = []
        if os.path.isfile(os.path.join(cdir, 'index.md')):
            entries.append(('About These Notebooks', 'index.md'))
        for label, nb in colab:
            if os.path.isfile(os.path.join(cdir, nb)):
                entries.append((label, nb))
            else:
                print('  drop (notebook absent): colab-nb/%s' % nb)
        # any notebook not named in SUMMARY still gets listed, so none is lost
        named = {n for _, n in entries}
        for nb in sorted(f for f in os.listdir(cdir) if f.endswith('.ipynb')):
            if nb not in named:
                entries.append((nb[:-6], nb))
                print('  added unlisted notebook: %s' % nb)
        if entries:
            write_pages(os.path.join(cdir, '.pages'), 'Google Colab Notebooks', entries)
            print('wrote colab-nb/.pages  (%d entries)' % len(entries))
            written += 1
            order.append('colab-nb')

    # --- top level ---
    top = []
    if os.path.isfile(os.path.join(docs, 'index.md')):
        top.append(('Home', 'index.md'))
    top += [(f, f) for f in order]
    if top:
        lines = ['nav:']
        for label, target in top:
            lines.append('  - %s' % target if label == target else
                         '  - %s: %s' % (yq(label), target))
        lines.append('  - ...')          # SAFETY: never hide a folder
        with open(os.path.join(docs, '.pages'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(lines) + '\n')
        print('wrote docs/.pages  (%d entries)' % len(top))

    print('--- generated %d .pages files, skipped %d folders ---' % (written, skipped))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:                      # never break the sync
        print('gen_mkdocs_pages.py failed (%s: %s)' % (type(exc).__name__, exc))
        print('Navigation will fall back to automatic ordering. Sync continues.')
        sys.exit(0)

