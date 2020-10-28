# chartree
Grow your own trees on a monospace grid. Choose the material (unicode) for your tree as well as the hue of the sky (also unicode). Heaps of other parameters as well!

## Example
import chartree as ct
w = ct.Ecosystem(material='7', background='.')

_// Grows a new tree each time_
w.grow(n_iter=50, ang_mean=40, ang_range=10)

_// Shows current tree. Can be used to experiment with materials_
w.show(material='#', background='i')