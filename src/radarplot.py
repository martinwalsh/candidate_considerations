#!/usr/bin/env python

# stolen shamelessly, and adapted, from http://stackoverflow.com/a/24669479/780220
import numpy as np
import pylab as pl  # noqa


class Radar(object):

    def __init__(self, fig, titles, labels, rect=None):
        if rect is None:
            rect = [0.05, 0.05, 0.95, 0.95]

        self.n = len(titles)
        self.angles = np.degrees(np.arange(0.0, 2*np.pi, 2*np.pi/self.n))
        # self.angles = np.arange(90, 90+360, 360.0/self.n)
        self.axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i) for i in range(self.n)]

        self.ax = self.axes[0]
        self.ax.set_thetagrids(self.angles, labels=titles, fontsize=11, rotation=0)

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid('off')
            ax.xaxis.set_visible(False)

        for ax, angle, label in zip(self.axes, self.angles, labels):
            ax.set_rgrids(range(1, 10), angle=angle, labels='')
            ax.spines["polar"].set_visible(False)
            ax.set_ylim(0, 10)

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)
        self.ax.fill(angle, values, alpha=0.15)


# similarly stolen from http://matplotlib.org/examples/api/radar_chart.html

"""
from radarplot import radar_factory

spoke_labels = df.Topic.unique()
theta = radar_factory(len(spoke_labels))

fig = pylab.figure(figsize=(12, 10))
ax = fig.add_subplot(1, 1, 1, projection='radar')
#pylab.rgrids([range(0, n.max()) for n in df[df.Company == 'Ideal'].Score])
for company in companies[1:]:
    scores = df[df.Company == company].Score
    ax.plot(theta, scores, label=company)
    ax.fill(theta, scores, alpha=0.25, label='')
ax.set_varlabels(spoke_labels, frac=1.10)
_ = ax.axes.yaxis.set_ticklabels([])
_ = ax.legend(loc=9, bbox_to_anchor=(1.05, 0.10))
"""

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.path import Path
# from matplotlib.spines import Spine
# from matplotlib.projections.polar import PolarAxes
# from matplotlib.projections import register_projection
#

# def unit_poly_verts(theta):
#     """Return vertices of polygon for subplot axes.

#     This polygon is circumscribed by a unit circle centered at (0.5, 0.5)
#     """
#     x0, y0, r = [0.5] * 3
#     verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
#     return verts

# def radar_factory(num_vars, frame='circle'):
#     """Create a radar chart with `num_vars` axes.

#     This function creates a RadarAxes projection and registers it.

#     Parameters
#     ----------
#     num_vars : int
#         Number of variables for radar chart.
#     frame : {'circle' | 'polygon'}
#         Shape of frame surrounding axes.

#     """
#     # calculate evenly-spaced axis angles
#     theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
#     # rotate theta such that the first axis is at the top
#     theta += np.pi/2

#     def draw_poly_patch(self):
#         verts = unit_poly_verts(theta)
#         return plt.Polygon(verts, closed=True, edgecolor='k')

#     def draw_circle_patch(self):
#         # unit circle centered on (0.5, 0.5)
#         return plt.Circle((0.5, 0.5), 0.5)

#     patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
#     if frame not in patch_dict:
#         raise ValueError('unknown value for `frame`: %s' % frame)

#     class RadarAxes(PolarAxes):

#         name = 'radar'
#         # use 1 line segment to connect specified points
#         RESOLUTION = 1
#         # define draw_frame method
#         draw_patch = patch_dict[frame]

#         def fill(self, *args, **kwargs):
#             """Override fill so that line is closed by default"""
#             closed = kwargs.pop('closed', True)
#             return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

#         def plot(self, *args, **kwargs):
#             """Override plot so that line is closed by default"""
#             lines = super(RadarAxes, self).plot(*args, **kwargs)
#             for line in lines:
#                 self._close_line(line)

#         def _close_line(self, line):
#             x, y = line.get_data()
#             # FIXME: markers at x[0], y[0] get doubled-up
#             if x[0] != x[-1]:
#                 x = np.concatenate((x, [x[0]]))
#                 y = np.concatenate((y, [y[0]]))
#                 line.set_data(x, y)

#         def set_varlabels(self, labels, frac=1.0, rotation=0, fontsize=None):
#             self.set_thetagrids(np.degrees(theta), labels, frac=frac, rotation=rotation, fontsize=fontsize)

#         def _gen_axes_patch(self):
#             return self.draw_patch()

#         def _gen_axes_spines(self):
#             if frame == 'circle':
#                 return PolarAxes._gen_axes_spines(self)
#             # The following is a hack to get the spines (i.e. the axes frame)
#             # to draw correctly for a polygon frame.

#             # spine_type must be 'left', 'right', 'top', 'bottom', or `circle`.
#             spine_type = 'circle'
#             verts = unit_poly_verts(theta)
#             # close off polygon by repeating first vertex
#             verts.append(verts[0])
#             path = Path(verts)

#             spine = Spine(self, spine_type, path)
#             spine.set_transform(self.transAxes)
#             return {'polar': spine}

#     register_projection(RadarAxes)
#     return theta
