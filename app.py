import streamlit as st

# Define la interfaz de usuario con Streamlit
def main():

    st.title("Sistema de Recomendacion de peliculas")

    st.write('Seleccione uno o varios generos')
    options = ['Terror', 'Drama', 'Aventura', 'Romantica']
    selected_options = st.multiselect('Selecciona las opciones:', options, max_selections=3)

    options = ['Opción 1', 'Opción 2', 'Opción 3']
    selected_option = st.selectbox('Selecciona una opción:', options)

    texto_usuario = st.text_input("Texto agregado por el ususario")
    
    if st.button("Enviar"):
        st.write(f'Opciones Seleccionadas: {selected_options}')
        st.write(f'Opcion: {selected_option}')
        st.write(f'Ingreso del ususario: {texto_usuario}')
    
if __name__ == "__main__":
    main()
