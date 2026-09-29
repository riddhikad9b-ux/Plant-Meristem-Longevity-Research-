import gradio as gr, pandas as pd, py3dmol
df = pd.read_csv('research_matrix.csv')
filter_matrix = lambda kw: df if not kw else df[df['Gene_Pathway'].str.contains(kw, case=False, na=False)]
def render_pdb(p):
    try:
        v = py3dmol.view(width=700, height=500)
        v.addModel(open(p).read(), 'pdb')
        v.setStyle({'cartoon': {'color': 'spectrum'}})
        v.zoomTo()
        return f'<iframe style="width: 100%; height: 520px; border: none;" srcdoc="{v._make_html()}"></iframe>'
    except Exception as e:
        return str(e)
with gr.Blocks() as demo:
    gr.Markdown('# 🌱 Plant Meristem Longevity Research Lab')
    with gr.Tabs():
        with gr.TabItem('Literature Matrix'):
            s = gr.Textbox(label='Filter')
            t = gr.Dataframe(value=df)
            s.change(fn=filter_matrix, inputs=s, outputs=t)
        with gr.TabItem('3D View'):
            gr.HTML(value=render_pdb('1lcd.pdb'))
demo.launch(inline=False, share=True)