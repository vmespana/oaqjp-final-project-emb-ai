"""
Módulo del servidor Flask para la aplicación de detección de emociones.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analiza el texto enviado por el usuario y devuelve las emociones detectadas.
    """
    # Obtiene el texto a analizar desde los argumentos de la URL
    text_to_analyze = request.args.get('textToAnalyze')
    # Llama a la función de detección
    response = emotion_detector(text_to_analyze)

    # Si la respuesta es None (texto vacío o error), devuelve un mensaje de error
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Formatea la respuesta exitosa
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

