
# Chapter 15: Matplotlib

The online companion to Chapter 15 of the book. Matplotlib is the library Python uses to draw: line charts, bar charts, scatter plots, histograms and a good deal more. The printed chapter introduces the figure, the axes and the common plot types. These pages carry forty conceptual questions, twenty-two scripting questions, and a set of pages on the parts that need more room — choosing the right plot for your data, grid data, and plotting in three dimensions.

By the end of these pages you should be able to pick a plot type from the shape of your data rather than by habit, tell the two Matplotlib interfaces apart and know why the object-oriented one is worth the extra line, read and write `np.meshgrid()`, and draw a surface in three dimensions.

You need Chapter 11 (NumPy) first. Most plots are drawn from arrays.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Data Types and Choosing the Right Plot](010-ch15-data-types.md) | The kinds of data there are, which plot suits each, and why the choice comes first | Start here |
| [Coordinate Data and Grid (Matrix) Data](020-ch15-grid-matrix.md) | The difference between points scattered in space and values on a regular grid, with a full worked project in two parts | After the chapter |
| [Violin Plots](050-ch15-violin1.md) | Seeing the shape of a distribution, and how a violin plot differs from a box plot | When a box plot hides too much |
| [Stem Plots](060-ch15-matplotlib-stem-plot1.md) | Showing individual values clearly, and when this beats a line or a bar | Discrete data |
| [Introduction to 3D Plotting](090-ch15-3d-plot.md) | Which plots work in 2D only, which work in both, which are made for 3D, and `np.meshgrid()` explained properly | After the 2D work |
| [Conceptual Questions and Answers](069-ch15-conceptual-qa-main1.md) | Twenty questions on how Matplotlib is put together | Revision |
| [Conceptual Questions: Deeper Level](070-ch15-conceptual-qa.md) | Twenty harder questions | After the first set |
| [Scripting Questions and Answers](080-ch15-scripting-qa.md) | Twenty-two programs to write, each with its figure | Practice |

## Suggested Reading Order

1. **Data Types and Choosing the Right Plot.** This comes first for a reason: most bad charts are the wrong chart drawn well. The page starts from the data and works towards the plot, which is the right direction.
2. **Coordinate Data and Grid Data.** The distinction between scattered points and a regular grid decides which functions you can use, and it is the idea behind `meshgrid`, contours and surfaces.
3. **Violin Plots** and **Stem Plots** as and when the data calls for them.
4. **3D Plotting**, once the 2D work is comfortable. The `np.meshgrid()` section is the part to read slowly.
5. **The two conceptual sets**, then the **scripting questions** as practice.

## Three Points Worth Extra Care

**There are two ways to use Matplotlib, and mixing them causes confusion.** The `plt.` shortcut draws on whatever figure is "current"; the object-oriented style, `fig, ax = plt.subplots()` and then `ax.plot(...)`, says exactly which axes you mean. The first is quicker for one chart; the second is the only sane choice once a figure has more than one panel. The conceptual questions cover the difference.

**A figure is not the same as an axes.** The figure is the whole picture; the axes is one set of x and y within it, and a figure can hold several. Almost every "why did my second plot appear on top of the first?" question comes from this.

**`np.meshgrid()` turns two 1D arrays into two 2D grids.** It is the step between "here are my x values and my y values" and "here is a value at every point". The 3D page works through it position by position; it is worth the time, because contour plots, heatmaps and surfaces all depend on it.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell.

Matplotlib does not come with Python. Install it once with `pip install matplotlib`. Some pages also use NumPy, and a few use `seaborn` for a dataset.

Two notes on running the scripts. In a plain `.py` file you need `plt.show()` at the end or nothing appears; in a notebook the figure is drawn for you. And the exact appearance of a chart — fonts, default colours, figure size — depends on your Matplotlib version and settings, so your picture may differ in small ways from the one on the page while being entirely correct.
