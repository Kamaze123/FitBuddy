function MessageBubble({ message, sender }) {
    const isUser = sender === "user";

    return(
        <div className = {`flex ${isUser ? "justify-end" : "justify-start"} mb-3`}>
            <div className = {`px-4 py-2 rounded-xl max-w-[75%] sm:max-w-[60%] md:max-w-[50%] text-sm sm:text-base
                 ${isUser ? "bg-blue-400" : "bg-gray-600"}`}>
                {message}
            </div>
        </div>
    );
}

export default MessageBubble;