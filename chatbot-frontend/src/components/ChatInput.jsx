import { useState } from "react";

function ChatInput({ sendMessage }) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    sendMessage(input);
    setInput("");
  };

  return (
    <div className="flex items-center gap-2 bg-zinc-900 border border-zinc-700 focus-within:border-zinc-500 transition-colors px-3 sm:px-4 py-2.5 rounded-2xl">
      <input
        className="flex-1 bg-transparent outline-none text-sm sm:text-base text-white placeholder-zinc-500"
        placeholder="Ask FitBuddy..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
      />
      <button
        className="bg-blue-500 hover:bg-blue-600 active:scale-95 transition-all px-3 sm:px-4 py-1.5 rounded-xl text-sm sm:text-base font-medium shrink-0"
        onClick={handleSend}
      >
        Send
      </button>
    </div>
  );
}

export default ChatInput;