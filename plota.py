import plotly.graph_objects as go

def create_plot(df, altura,tipo_de_mapa='Contorno', escala_de_cor='Turbo', contorno=None,titulo_barra=True,titulo='',lacunas=True):

    # Criar o dicionário base para o Contour
    contour_dict = {
        'x': df[df.columns[0]],
        'y': df[df.columns[1]],
        'z': df[df.columns[2]],
        'connectgaps': lacunas,
        'colorscale': escala_de_cor,
    }

    if titulo_barra:
            contour_dict['colorbar'] = {"title": df.columns[2]}

    match tipo_de_mapa:
                case 'Contorno':
                    contour_dict['contours'] = {"showlines": contorno}
                    fig = go.Figure(data =go.Contour(**contour_dict))
                case 'Calor':
                      fig = go.Figure(data =go.Heatmap(**contour_dict))
                                
            
            # Atualizar legendas e tamanho da fonte dos eixos
    fig.update_layout(
            xaxis_title=df.columns[0],
            yaxis_title=df.columns[1],
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            ),
            height=altura,
            title={
                   'text':titulo,
                   'xanchor': 'right',
                   'x': 0.6,
                   'yanchor': 'top'
                   }
            
                
    )
    return fig