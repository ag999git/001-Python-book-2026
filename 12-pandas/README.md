# Chapter 12: pandas

The online companion to Chapter 12 of the book. pandas is the tool for working with data in tables: reading a file, cleaning it, filtering it, grouping it and summarising it. The printed chapter introduces the Series and the DataFrame. These pages carry fifty-five conceptual questions, thirty script exercises, and a run of projects that take one real dataset from first look to finished analysis.

By the end of these pages you should be able to load a file and find out what is in it, select rows and columns without guessing between `loc` and `iloc`, deal with missing values sensibly rather than deleting them, group and summarise, and join two tables together.

You need Chapter 11 (NumPy) first, since a DataFrame is built on arrays.

## Foundations

| Page | What it covers | Best for |
| --- | --- | --- |
| [Methods of Series: The Four Pillars](10-ch12-series-methods.md) | The Series, the building block of everything else, and its four families of method | Start here |
| [How DataFrames Are Created](20-ch12-dataframe-creation.md) | Every way to build a DataFrame: from lists, dictionaries, arrays and files | After the Series |
| [Memory-Based I/O](30-ch12-io-module.md) | Reading and writing data held in memory rather than on disk, with `StringIO` | When you want to test without files |

## Working With a Real Dataset

These nine pages use the Palmer Penguins dataset and build on each other. Read them in order and you have done a complete analysis.

| Page | What it covers |
| --- | --- |
| [Essential Data Exploration](35-ch12-essential-data-exploration.md) | The first half hour with any dataset: shape, dtypes, `head()`, `describe()`, `info()` |
| [Indexing and Selection](40-ch12-indexing-selection.md) | `loc`, `iloc` and plain brackets, and which to reach for |
| [Conditional Filtering](50-ch12-conditional-filtering.md) | Selecting rows by a condition, and combining conditions |
| [Handling Missing Values](60-ch12-missing-values.md) | Finding them, understanding why they are there, and deciding what to do |
| [Data Cleaning: Structural Changes](70-ch12-data-cleaning-structural-change.md) | Renaming, retyping and reshaping columns into a usable form |
| [Deriving Metrics, Removing Columns and Sorting](80-ch12-deriving-matrices.md) | Making new columns from old ones, and putting the table in order |
| [Grouping and Aggregation](90-ch12-grouping-aggregate.md) | `groupby()`, the single most useful thing pandas does |
| [Merging and Joining Data](93-ch12-merging-joining-data.md) | Putting two tables together, and the four kinds of join |
| [Hierarchical Analysis with MultiIndex](97-ch12-pivot-analysis.md) | Pivot tables and indexes with more than one level |

## Further Topics

| Page | What it covers |
| --- | --- |
| [Time Series Basics](95-ch12-time-series.md) | Dates as an index, resampling, and rolling windows |
| [Reading JSON: the orient Parameter](98-ch12-orient-json.md) | Why the same JSON file can load four different ways |
| [One DataFrame, Four JSON Formats](99-0-ch12-orient-json2.md) | The same idea from the other direction, step by step |
| [Project: Exploring the Palmer Penguins Dataset](99-1-palmer-penguin-analysis.md) | The whole analysis in one place, start to finish |

## Questions

| Page | What it covers |
| --- | --- |
| [Conceptual Questions: A Study Companion](99-2-ch12-conceptualQ.md) | Fifty-five questions on how pandas works and why |
| [30 Script Questions](99-3-ch12-scriptQ.md) | Thirty programs to write, each with a worked answer |

## Suggested Reading Order

1. **Series methods**, then **How DataFrames Are Created**. A DataFrame is a set of Series sharing an index, and that idea explains a great deal later.
2. **The nine penguin pages, in order.** They are a course in themselves: the same dataset, explored, selected from, cleaned, extended, grouped and joined. Do not skip **Essential Data Exploration** — knowing what is in a file before you touch it is most of the skill.
3. **The Conceptual Questions** alongside, a few at a time.
4. **The 30 Script Questions** as practice once the penguin pages are done.
5. **Time series, JSON and the full penguin project** last, as and when you need them.

## Three Points Worth Extra Care

**`loc` uses labels, `iloc` uses positions.** `df.loc[0]` asks for the row labelled 0; `df.iloc[0]` asks for the first row. They are often the same row, which is exactly why the difference is easy to miss until the day it bites.

**Most pandas operations return a new object and leave the original alone.** `df.dropna()` does not change `df`. Keep the result, or the work is lost. The `inplace=True` argument exists but is discouraged in modern pandas.

**A missing value is information.** `NaN` may mean "not measured", "not applicable" or "lost". Dropping every row with a missing value is quick and often wrong. The missing-values page works through the judgement.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell.

pandas does not come with Python. Install it once with `pip install pandas`. Some pages also use Matplotlib for plots and `seaborn` for the penguins dataset.

Two things will differ on your machine. Timing comparisons depend on your hardware, so only the size of the difference is meant to match. And pandas changes between versions: if an output looks slightly different from the page, check your version with `pd.__version__` before assuming something is wrong.

