import React, { useState } from 'react';

function Quiz({ questions }) {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [showResults, setShowResults] = useState(false);

  const handleAnswer = (answer) => {
    setUserAnswers({ ...userAnswers, [currentQuestion]: answer });
  };

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      setShowResults(true);
    }
  };

  const calculateScore = () => {
    let score = 0;
    questions.forEach((q, index) => {
      if (userAnswers[index] === q.correct_answer) {
        score++;
      }
    });
    return score;
  };

  if (showResults) {
    const score = calculateScore();
    return (
      <div>
        <h2>Quiz Results</h2>
        <p>You scored {score} out of {questions.length}</p>
        {questions.map((q, index) => (
          <div key={index}>
            <p>{q.question}</p>
            <p>Your answer: {userAnswers[index]}</p>
            <p>Correct answer: {q.correct_answer}</p>
          </div>
        ))}
      </div>
    );
  }

  const question = questions[currentQuestion];

  return (
    <div>
      <h2>Question {currentQuestion + 1}</h2>
      <p>{question.question}</p>
      {question.options.map((option, index) => (
        <button
          key={index}
          onClick={() => handleAnswer(option)}
          disabled={userAnswers[currentQuestion]}
        >
          {option}
        </button>
      ))}
      <button onClick={handleNext}>
        {currentQuestion < questions.length - 1 ? 'Next' : 'Finish'}
      </button>
    </div>
  );
}

export default Quiz;
