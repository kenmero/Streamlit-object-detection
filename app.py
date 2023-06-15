import streamlit as st
from utils import azureapi
from utils import image

st.title('物体検出アプリ')

uploaded_file = st.file_uploader('Choose an image ...', type=['jpg', 'png'])
if uploaded_file is not None:
    image = image.ImageMan(uploaded_file)
    image.save_img_file()

    for local_image in azureapi.read_local_image(image.file_path):
        results = azureapi.analyze_local_image(local_image)

        for x, y, w, h, caption in azureapi.get_detect_objects(results):
            image.draw_rectangle(x, y, w, h, outline='green', width=5)
            
            text_w, text_h = image.get_textsize(caption)
            image.draw_rectangle(x, y, text_w, text_h, fill='green')
            image.draw_text(x, y, caption)

        st.image(image.img)

        st.markdown('**認識されたコンテンツタグ**')
        tags = ', '.join(azureapi.get_local_tags(results))
        st.markdown(f'> {tags}')
