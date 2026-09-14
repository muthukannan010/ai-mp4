"use client";

import React, { useState } from 'react';

type Message = {
  role: 'user' | 'ai';
  content: string;
};

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [activeMenu, setActiveMenu] = useState("Projects");
  const [activeTopNav, setActiveTopNav] = useState("AI Director");
  const [showProfileMenu, setShowProfileMenu] = useState(false);

  const handleSend = () => {
    if (!prompt.trim()) return;
    
    // Add user message
    const newMessages: Message[] = [...messages, { role: 'user', content: prompt }];
    setMessages(newMessages);
    setPrompt("");

    // Simulate AI response
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        { 
          role: 'ai', 
          content: "I'll help you create that. Let me generate a storyboard and some characters for your idea." 
        }
      ]);
    }, 1000);
  };

  const handleQuickAction = (text: string) => {
    setPrompt((prev) => (prev ? `${prev} ${text}` : text));
  };

  const handleNewVideo = () => {
    setMessages([]);
    setPrompt("");
  };

  return (
    <div className="flex h-screen bg-[#F3F4F6] p-4 font-sans text-slate-800">
      {/* Sidebar */}
      <aside className="w-64 bg-white rounded-3xl shadow-sm flex flex-col overflow-hidden relative">
        <div className="p-6">
          <div className="flex items-center gap-3 mb-8">
            <div className="w-8 h-8 rounded-full bg-emerald-400 flex items-center justify-center text-white font-bold">
              C
            </div>
            <span className="font-bold text-xl tracking-tight">CineAI</span>
          </div>

          <button 
            onClick={handleNewVideo}
            className="w-full flex items-center justify-center gap-2 bg-slate-50 hover:bg-slate-100 text-slate-700 py-3 rounded-2xl border border-slate-100 font-medium transition-colors mb-8 active:scale-95"
          >
            <span>+</span> New Video
          </button>

          <div className="mb-6">
            <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">Project</h3>
            <ul className="space-y-1">
              {['Projects', 'Scenes', 'Characters', 'Assets'].map((item) => (
                <li key={item}>
                  <button 
                    onClick={() => setActiveMenu(item)}
                    className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg transition-colors ${activeMenu === item ? 'bg-emerald-50 text-emerald-700' : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'}`}
                  >
                    <div className={`w-4 h-4 rounded border ${activeMenu === item ? 'border-emerald-400 bg-emerald-100' : 'border-slate-300'}`}></div>
                    <span className="font-medium text-sm">{item}</span>
                  </button>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">History</h3>
            <ul className="space-y-2 text-sm text-slate-500">
              <li className="truncate hover:text-slate-800 cursor-pointer">Cinematic train station...</li>
              <li className="truncate hover:text-slate-800 cursor-pointer">Neon cyberpunk city...</li>
            </ul>
          </div>
        </div>

        {/* Bottom Profile */}
        <div className="mt-auto p-4 relative z-10">
          <div 
            onClick={() => setShowProfileMenu(!showProfileMenu)}
            className="bg-white/80 backdrop-blur-md border border-slate-100 rounded-2xl p-3 flex items-center gap-3 shadow-sm cursor-pointer hover:bg-slate-50 transition-colors"
          >
            <div className="w-10 h-10 rounded-full bg-slate-200"></div>
            <div className="flex-1 min-w-0">
              <p className="text-sm font-semibold text-slate-800 truncate">Creator</p>
              <p className="text-xs text-slate-500 truncate">studio@cineai.local</p>
            </div>
            <div className={`text-slate-400 transition-transform ${showProfileMenu ? 'rotate-180' : ''}`}>⌄</div>
          </div>
          
          {showProfileMenu && (
            <div className="absolute bottom-full left-4 right-4 mb-2 bg-white rounded-xl shadow-lg border border-slate-100 overflow-hidden z-20">
              <div className="p-2">
                <button className="w-full text-left px-3 py-2 text-sm text-slate-700 hover:bg-slate-50 rounded-lg transition-colors">Profile Settings</button>
                <button className="w-full text-left px-3 py-2 text-sm text-slate-700 hover:bg-slate-50 rounded-lg transition-colors">Sign Out</button>
              </div>
            </div>
          )}
        </div>
        {/* Decorative gradient for sidebar */}
        <div className="absolute bottom-0 left-0 right-0 h-48 bg-gradient-to-t from-emerald-100/50 to-transparent pointer-events-none"></div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col ml-4 bg-white rounded-3xl shadow-sm overflow-hidden relative">
        {/* Top Navigation */}
        <header className="h-20 border-b border-slate-50 flex items-center justify-between px-8 shrink-0">
          <nav className="flex items-center gap-2 bg-slate-50 p-1 rounded-full">
            {['Dashboard', 'AI Director', 'Help', 'Settings'].map((item) => (
              <button 
                key={item}
                onClick={() => setActiveTopNav(item)}
                className={`px-6 py-2 text-sm font-medium rounded-full transition-colors ${activeTopNav === item ? 'bg-white text-slate-900 shadow-sm' : 'text-slate-500 hover:text-slate-800'}`}
              >
                {item}
              </button>
            ))}
          </nav>
          
          <div className="flex items-center gap-4">
            <button className="flex items-center gap-2 bg-slate-50 hover:bg-slate-100 px-4 py-2 rounded-full text-sm font-medium text-slate-600 transition-colors">
              <span>Untitled Film</span>
            </button>
            <div className="w-8 h-8 rounded-full bg-slate-200"></div>
          </div>
        </header>

        {/* Main Content Area Based on Top Nav */}
        <div className="flex-1 flex flex-col items-center p-8 relative overflow-hidden">
          {activeTopNav === 'AI Director' ? (
            activeMenu === 'Projects' ? (
              <>
                <div className="flex-1 w-full max-w-3xl overflow-y-auto mb-8 pr-4 flex flex-col gap-6">
                  {messages.length === 0 ? (
                    <div className="m-auto text-center">
                      <h1 className="text-4xl font-bold text-slate-800 mb-8">Hey, I'm CineAI Director. <br/> What are we creating today?</h1>
                      
                      <div className="flex items-center justify-center gap-4">
                        <button onClick={() => handleQuickAction("Storyboard")} className="px-4 py-2 bg-slate-50 hover:bg-slate-100 text-slate-600 text-sm font-medium rounded-full flex items-center gap-2 transition-colors border border-slate-100 active:scale-95">
                          <span>⚡</span> Storyboard
                        </button>
                        <button onClick={() => handleQuickAction("30 Seconds")} className="px-4 py-2 bg-slate-50 hover:bg-slate-100 text-slate-600 text-sm font-medium rounded-full flex items-center gap-2 transition-colors border border-slate-100 active:scale-95">
                          <span>⏱️</span> 30 Seconds
                        </button>
                        <button onClick={() => handleQuickAction("Cinematic style")} className="px-4 py-2 bg-slate-50 hover:bg-slate-100 text-slate-600 text-sm font-medium rounded-full flex items-center gap-2 transition-colors border border-slate-100 active:scale-95">
                          <span>🎨</span> Cinematic
                        </button>
                      </div>
                    </div>
                  ) : (
                    <div className="flex flex-col gap-6 w-full pt-4">
                      {messages.map((msg, index) => (
                        <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                          <div className={`max-w-[80%] rounded-2xl p-4 ${msg.role === 'user' ? 'bg-emerald-500 text-white rounded-br-none' : 'bg-slate-50 text-slate-800 border border-slate-100 rounded-bl-none'}`}>
                            <p className="text-sm leading-relaxed">{msg.content}</p>
                          </div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>

                {/* Input Box */}
                <div className="w-full max-w-3xl shrink-0">
                  <div className="relative w-full">
                    <div className="bg-slate-50/80 backdrop-blur-sm border border-emerald-100/50 rounded-3xl p-4 shadow-sm relative z-10 flex flex-col gap-3">
                      <div className="flex items-center gap-3">
                        <button className="w-8 h-8 rounded-full hover:bg-slate-200 flex items-center justify-center text-slate-500 transition-colors">
                          +
                        </button>
                        <input 
                          type="text" 
                          value={prompt}
                          onChange={(e) => setPrompt(e.target.value)}
                          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                          placeholder="Describe your story, scene, character..." 
                          className="flex-1 bg-transparent border-none outline-none text-slate-700 placeholder-slate-400 text-lg"
                        />
                      </div>
                      
                      <div className="flex items-center justify-between mt-2 pt-2 border-t border-slate-100/50">
                        <div className="flex items-center gap-2">
                          <button className="px-3 py-1.5 bg-white text-slate-600 text-xs font-semibold rounded-lg shadow-sm border border-slate-100 flex items-center gap-1 hover:bg-slate-50 transition-colors">
                            <span>✨</span> Auto
                          </button>
                          <button className="p-2 text-slate-400 hover:text-slate-600 transition-colors">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" x2="12" y1="19" y2="22"></line></svg>
                          </button>
                        </div>
                        
                        <button 
                          onClick={handleSend}
                          disabled={!prompt.trim()}
                          className="bg-emerald-400 hover:bg-emerald-500 disabled:opacity-50 disabled:hover:bg-emerald-400 text-white px-5 py-2 rounded-xl font-medium shadow-sm shadow-emerald-200 transition-all flex items-center gap-2 active:scale-95"
                        >
                          Send <span>↑</span>
                        </button>
                      </div>
                    </div>
                    {/* Soft glow behind input */}
                    <div className="absolute inset-0 bg-emerald-200/20 blur-3xl -z-10 rounded-full transform translate-y-4"></div>
                  </div>
                </div>
              </>
            ) : (
              <div className="m-auto text-center">
                <h1 className="text-3xl font-bold text-slate-400">{activeMenu}</h1>
                <p className="text-slate-500 mt-4">This section is currently under construction.</p>
              </div>
            )
          ) : (
            <div className="m-auto text-center">
              <h1 className="text-3xl font-bold text-slate-400">{activeTopNav}</h1>
              <p className="text-slate-500 mt-4">This section is currently under construction.</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
