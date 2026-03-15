function MessageBubble({ message, sender }) {
  const isUser = sender === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-3`}>
      <div
        className={`px-4 py-2.5 rounded-2xl max-w-[85%] sm:max-w-[70%] md:max-w-[60%]
          text-sm sm:text-base leading-relaxed
          ${isUser ? "bg-blue-600 text-white" : "bg-zinc-800 text-zinc-100"}`}
      >
        {message}
      </div>
    </div>
  );
}

export default MessageBubble;