import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import PDFUpload from './components/PDFUpload';
import Quiz from './components/Quiz';

function App() {
  const [quizQuestions, setQuizQuestions] = useState(null);

  const handlePDFUpload = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/api/pdf-documents/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setQuizQuestions(response.data.quiz_questions);
    } catch (error) {
      console.error('Error uploading PDF:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>PDF Quiz Generator</h1>
        {!quizQuestions ? (
          <PDFUpload onUpload={handlePDFUpload} />
        ) : (
          <Quiz questions={quizQuestions} />
        )}
      </header>
    </div>
  );
}

export default App;
