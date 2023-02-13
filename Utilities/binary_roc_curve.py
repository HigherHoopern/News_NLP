# plot ROC AUC curve 
from sklearn.metrics import roc_curve, auc
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go
import chart_studio.plotly as py
import plotly.figure_factory as ff
import plotly.offline as py
py.init_notebook_mode()
import cufflinks

def ROC_curve(y_true, y_score,chart_name):
    
    y_true = np.array(y_true)
    y_score = np.array(y_score)
    
    fpr, tpr, thresholds = roc_curve(y_true, y_score)

    fig = px.area(
        x=fpr, y=tpr,
        title=f'{chart_name} ROC Curve (AUC={auc(fpr, tpr):.4f})'.format(chart_name=chart_name),
        labels=dict(x='False Positive Rate', y='True Positive Rate'),
        width=700, height=500)
    fig.add_shape(
        type='line', line=dict(dash='dash'),
        x0=0, x1=1, y0=0, y1=1)

    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig.update_xaxes(constrain='domain')
    fig.show()