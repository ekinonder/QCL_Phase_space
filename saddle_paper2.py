import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

f=open('circuit56_9.txt','r')
f1=open('circuit5695.txt','r')
f2=open('circuit57_0.txt','r')
data=np.loadtxt(f)
data1=np.loadtxt(f1)
data2=np.loadtxt(f2)

t=data[:,0]
x=data[:,1]

t1=data1[:,0]
x1=data1[:,1]

t2=data2[:,0]
x2=data2[:,1]

n11=750000
n22=800000
pi=3.141516
#plt.show()
x=x
print(len(x))
n1=1000
n2=len(x)
x=x[-50000:]
t=t[-50000:]

x1=x1[-50000:]
t1=t1[-50000:]

x2=x2[-50000:]
t2=t2[-50000:]

dxdt=np.diff(x)/np.diff(t)
ddxt=np.diff(dxdt)/np.diff(t[0:-1])
#ax.plot(x[0:len(x)-1],dxdt)

dxdt1=np.diff(x1)/np.diff(t1)
ddxt1=np.diff(dxdt1)/np.diff(t1[0:-1])

dxdt2=np.diff(x2)/np.diff(t2)
ddxt2=np.diff(dxdt2)/np.diff(t2[0:-1])



fig = plt.figure(figsize = (12,12))
#fig.text(0.5, 0.04, c, ha='center',fontsize=16)
#fig.text(0.0, 0.5, '$dU/dt$', va='center', rotation='vertical',fontsize=16)
# set height ratios for sublots
gs = gridspec.GridSpec(3, 2) 

# the fisrt subplot
ax0 = plt.subplot(gs[0])
# log scale for axis Y of the first subplot

line0, = ax0.plot(x[0:-1], dxdt, color='r', label='$56.90$ $V$')

#the second subplot
# shared axis X
ax1 = plt.subplot(gs[2], sharex = ax0)
line1, = ax1.plot(x1[0:-1], dxdt1, color='b', linestyle='-', label='$56.95$ $V$')
plt.setp(ax0.get_xticklabels(), visible=False)
# remove last tick label for the second subplot
yticks = ax0.yaxis.get_major_ticks()
yticks[0].label1.set_visible(False)

ax5 = plt.subplot(gs[4], sharex = ax1)
line2, = ax5.plot(x2[0:-1], dxdt2, color='m', linestyle='-', label='$57.00$ $V$')
plt.setp(ax1.get_xticklabels(), visible=False)
# remove last tick label for the second subplot
yticks = ax1.yaxis.get_major_ticks()
yticks[0].label1.set_visible(False)


# put lened on first subplot
#ax0.legend((line0, line1,line2), ('$56.90$ $V$', '$56.95$ $V$','$57.0$ $V$'), loc='lower left',fontsize=20)

ax2=plt.subplot(gs[1])
ax2.plot(x[0:-1], dxdt, color='r')
ax3=plt.subplot(gs[3], sharex=ax2)
ax3.plot(x1[0:-1], dxdt1, color='b')
plt.setp(ax2.get_xticklabels(), visible=False)
ax4=plt.subplot(gs[5], sharex=ax3)
ax4.plot(x2[0:-1], dxdt2, color='m')
plt.setp(ax3.get_xticklabels(), visible=False)
yticks = ax4.yaxis.get_major_ticks()
yticks[-1].label1.set_visible(False)


ax0.legend(loc='lower left',fontsize=35)
ax1.legend(loc='lower left',fontsize=35)
ax5.legend(loc='lower left',fontsize=35)

#xticks=np.arange(10.0,14.0,1)
#ax5.set_xticks(xticks)

yticks = np.arange(-0.15, 0.15, 0.05)
ax0.set_yticks(yticks)
ax1.set_yticks(yticks)
ax5.set_yticks(yticks)

# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)
plt.setp(ax1.get_xticklabels(), fontsize=25)
plt.setp(ax1.get_yticklabels(), fontsize=25)
plt.setp(ax0.get_xticklabels(), fontsize=25)
plt.setp(ax0.get_yticklabels(), fontsize=25)
plt.setp(ax3.get_xticklabels(), fontsize=25)
plt.setp(ax3.get_yticklabels(), fontsize=25)
plt.setp(ax2.get_xticklabels(), fontsize=25)
plt.setp(ax2.get_yticklabels(), fontsize=25)
plt.setp(ax4.get_xticklabels(), fontsize=25)
plt.setp(ax4.get_yticklabels(), fontsize=25)
plt.setp(ax5.get_xticklabels(), fontsize=25)
plt.setp(ax5.get_yticklabels(), fontsize=25)



ax1.set_xlabel('QCL Voltage $U_{qcl}$ ($V$)',fontsize=30)
ax3.set_xlabel('QCL Voltage $U_{qcl}$ ($V$)',fontsize=30)
ax4.set_xlabel('QCL Voltage $U_{qcl}$ ($V$)',fontsize=30)
ax5.set_xlabel('QCL Voltage $U_{qcl}$ ($V$)',fontsize=30)

ax0.set_ylabel('$dU_{qcl}/dt$',fontsize=30)
ax1.set_ylabel('$dU_{qcl}/dt$',fontsize=30)
ax5.set_ylabel('$dU_{qcl}/dt$',fontsize=30)
#ax1.xaxis.labelpad = 10
ax0.set_xlim([9.75,13.25])
#ax0.set_ylim([0,950])
#ax1.set_ylim([700,770])
ax1.set_xlim([9.75,13.25])
ax2.set_xlim([11,11.5])
ax2.set_ylim([-0.025,0.025])
ax3.set_xlim([11,11.5])
ax3.set_ylim([-0.025,0.025])
ax4.set_xlim([11,11.5])
ax4.set_ylim([-0.025,0.025])




point=11.19 ,0.001
circle_rad = 11.5  # This is the radius, in points
ax2.plot(11.19,0.001, 'o',
        ms=circle_rad * 2, mec='g', mfc='none', mew=4)
ax2.annotate('Saddle p.', xy=point, xytext=(50, -40),
            textcoords='offset points',
            color='g', size='large',
            arrowprops=dict(
                arrowstyle='simple,tail_width=0.3,head_width=0.8,head_length=0.8',
                facecolor='r', shrinkB=circle_rad * .5),fontsize=25
)



#####ARROW PLOTS   AX2#######

ax2.annotate('', xy=(11.1, 0.005), xytext=(11.03, 0.01),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax2.annotate('', xy=(11.35, 0.015), xytext=(11.3, 0.01),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax2.annotate('', xy=(11.25, -0.01), xytext=(11.3, -0.015),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax2.annotate('', xy=(11.08, -0.013), xytext=(11.12, -0.008),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

#####ARROW PLOTS AX3######

ax3.annotate('', xy=(11.15, 0.006), xytext=(11.08, 0.015),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax3.annotate('', xy=(11.40, 0.017), xytext=(11.32, 0.01),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax3.annotate('', xy=(11.22, -0.005), xytext=(11.29, -0.015),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax3.annotate('', xy=(11.07, -0.011), xytext=(11.15, -0.003),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

####ARROW PLOTS AX4#########3

ax4.annotate('', xy=(11.15, 0.006), xytext=(11.08, 0.015),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax4.annotate('', xy=(11.40, 0.017), xytext=(11.32, 0.01),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax4.annotate('', xy=(11.22, -0.005), xytext=(11.29, -0.015),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

ax4.annotate('', xy=(11.07, -0.011), xytext=(11.15, -0.003),
            arrowprops=dict(facecolor='black',lw=0.08, shrink=0.03))

plt.show()






