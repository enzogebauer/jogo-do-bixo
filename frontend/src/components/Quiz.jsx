// components/Quiz.jsx
import React, { useState } from 'react';

export const Quiz = () => {
  const [questions, setQuestions] = useState('Qual é a capital do Brasil?');
  const [answers, setAnswers] = useState([
    'Rio de Janeiro',
    'São Paulo',
    'Brasília',
    'Salvador'
  ]);
  const [selectedAnswer, setSelectedAnswer] = useState('');

  const fetchQuestions = async () => {
    try {
      const response = await fetch('http://localhost:8000', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          method: 'get_list',
          params: [],
          id: 1,
        }),
      });
      const data = await response.json();
      setQuestions(data.result);
    } catch (error) {
      console.error("Erro ao buscar perguntas:", error);
    }
  };


  return (
    <div className="max-w-md mx-auto mt-8 p-6 bg-white shadow-md rounded-md">
      <h2 className="text-lg font-semibold mb-4">{question}</h2>
      <div>
        {answers.map((answer, index) => (
          <Button
            key={index}
            className={`p-4 mb-4 bg-blue-100 cursor-pointer ${selectedAnswer === answer ? 'bg-blue-300' : ''
              }`}
            onClick={() => handleAnswerClick(answer)}
          >
            {answer}
          </Button>
        ))}
      </div>
    </div>
  );
};

