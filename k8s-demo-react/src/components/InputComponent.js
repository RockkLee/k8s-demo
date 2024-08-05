import React, { useState } from 'react';

function InputComponent({ onFetchData }) { //"onFetchData" is a callback function
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = () => {
    onFetchData(inputValue);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div>
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        onKeyPress={handleKeyPress}
        style={{ marginRight: '10px' }}
      />
      <button onClick={handleSubmit}>Send</button>
    </div>
  );
}

export default InputComponent;
