import { useState } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

function ChatBox(){
    const [messages, setMessages] = useState([]);

    const sendMessage = async (text) => {

        const newMessages = [
            ...messages, 
            { sender : "user", text}
        ];

        setMessages(newMessages);

        setTimeout(() =>{
            setMessages(m => [
                ...m, 
                { sender: "bot", text: "I'm FitBuddy 💪" }
            ]);
        }, 500);
    };

    return(
    <div className="flex flex-col h-screen max-w-3xl mx-auto">

      <div className="flex-1 overflow-y-auto p-6">

        {messages.length === 0 && (
          <div className="text-center mt-32 text-2xl text-gray-300">
            Hello I am <span className="text-blue-400">FitBuddy</span>
            <br />
            Your AI fitness coach
          </div>
        )}

        {messages.map((msg, index) => (
          <MessageBubble
            key={index}
            message={msg.text}
            sender={msg.sender}
          />
        ))}

      </div>

      <div className="p-4">
        <ChatInput sendMessage={sendMessage} />
      </div>

    </div>
    );
}

export default ChatBox;