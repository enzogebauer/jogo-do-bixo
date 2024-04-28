// App.jsx
import React from 'react';
import { Quiz } from './components/Quiz';
import './App.css';

function App() {
  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gray-600">
      <h1 className="text-3xl font-semibold mt-8 mb-4">Quiz: Teste seus conhecimentos</h1>
      <Quiz />
      <p className="text-black mt-4">
        Clique na resposta que você acha que está correta.
      </p>
    </div>
  );
}

export default App;
