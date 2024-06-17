const answers = {
    "¿Cuál es tu nombre?": "Mi nombre es Chatbot.",
    "¿Qué hora es?": `La hora actual es ${new Date().toLocaleTimeString()}.`,
    "1"  : "PredatorGYM es un gimnasio dedicado a ofrecer las mejores instalaciones y programas de entrenamiento para ayudarte a alcanzar tus objetivos de fitness. Contamos con equipos de última generación, clases grupales, y entrenadores personales certificados para apoyarte en tu camino hacia una vida más saludable.",
    "2" : "PredatorGYM está ubicado en La cruz de taratara. Estamos convenientemente situados para que puedas acceder fácilmente a nuestras instalaciones. ¿Necesitas direcciones más detalladas?",
    "3" : "Ofrecemos una variedad de planes para adaptarnos a tus necesidades y horarios. Tenemos membresías mensuales, trimestrales y anuales, así como pases diarios. También ofrecemos paquetes especiales para estudiantes y familias.",
    "4" : "Nuestro equipo de entrenadores está compuesto por profesionales altamente calificados y certificados en diversas áreas del fitness. Cada uno de nuestros entrenadores está dedicado a ayudarte a alcanzar tus metas personales a través de programas de entrenamiento personalizados y asesoramiento continuo.",
    "5" : "En PredatorGYM, ofrecemos una amplia gama de rutinas de ejercicio para adaptarnos a tus necesidades y objetivos. Esto incluye rutinas de fuerza, cardio, entrenamiento funcional, yoga, pilates, y más. También tenemos programas específicos para pérdida de peso, ganancia muscular, y mejora de la resistencia.",
    "6" : "Puedes ponerte en contacto con nosotros a través de varios canales. Nuestro número de teléfono es +58 426-7402769, y nuestro correo electrónico es predatorgym@gmail.com. Tambien puedes acceder a la sección de contacto",
    // Agrega más preguntas cerradas y sus respuestas aquí
};


const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");

let userMessage = null; // Variable para almacenar el mensaje del usuario 
const inputInitHeight = chatInput.scrollHeight;

const createChatLi = (message, className) => {
// Crea un elemento de chat <li> con el mensaje pasado y el nombre de clase
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi; // return elemento chat <li> 
}



const generateResponse = () => {
   
        // Responder a la pregunta cerrada
    if (answers[userMessage]) {
        chatbox.innerHTML += `<li class="chat incoming">
        <span class="material-symbols-outlined">smart_toy</span>
        <p>${answers[userMessage]}</p>
      </li>`; 
    } 
    else {
        chatbox.innerHTML+= `<li class="chat incoming">
          <span class="material-symbols-outlined">smart_toy</span>
          <p>Lo siento, tiene que seleccionar unas de las opciones</p>
        </li>`;
    }
   
}


// ¿Cuál es tu nombre?

const handleChat = () => {
    userMessage = chatInput.value.trim(); // Recibe el mensaje ingresado por el usuario y elimina los espacios en blanco adicionales
    if(!userMessage) return;

// Borra el área de texto de entrada y establece su altura por defecto
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

// Agrega el mensaje del usuario al chatbox
    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
    
    setTimeout(() => {
        // Muestra el mensaje "Pensando..." mientras espera la respuesta
        generateResponse();    
        chatbox.scrollTo(0, chatbox.scrollHeight);
    }, 1000);

    setTimeout(() => {
    const again = createChatLi("Puedo ayudarte en algo mas??","incoming");
    chatbox.appendChild(again);
    chatbox.scrollTo(0, chatbox.scrollHeight);

    }, 2000);
}

chatInput.addEventListener("input", () => {
    //Ajusta la altura del área de texto de entrada según su contenido
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    // Si se presiona la tecla Enter sin la tecla Shift y la ventana
    // el ancho es mayor a 800px, maneja el chat
    if(e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendChatBtn.addEventListener("click", handleChat);
closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));

