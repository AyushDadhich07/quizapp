import React, { useState } from 'react';

function PDFUpload({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (file) {
      onUpload(file);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept=".pdf" onChange={handleFileChange} />
      <button type="submit" disabled={!file}>
        Upload PDF and Generate Quiz
      </button>
    </form>
  );
}

export default PDFUpload;
