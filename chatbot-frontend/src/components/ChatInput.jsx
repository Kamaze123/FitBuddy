import { useState } from "react";

function ChatInput({sendMessage}){
    
    const [input, setInput] = useState("");

    const handleSend = () => {
        if (!input.trim()) return;

        sendMessage(input);
        setInput("");
    };

    return(
        <div className="flex items-center gap-2 bg-zinc-800 p-3 rounded-xl">
            <input
                className="flex-1 bg-transparent outline-none"
                placeholder="Ask FitBuddy..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />

            <button className = "bg-blue-500 px-4 py-2 rounded-lg" onClick = {handleSend}>
                Send
            </button>
        </div>
    )
}

export default ChatInput;