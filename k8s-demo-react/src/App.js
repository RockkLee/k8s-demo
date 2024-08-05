import React, { useState } from 'react';
import InputComponent from './components/InputComponent';
import { fetchPostHeaderData, fetchGetData, fetchDeleteData } from './util/Api';

function App() {
  const [response, setResponse] = useState(null);

  const handleFetchData = async (inputValue) => {
    try {
      const data = await fetchPostHeaderData("http://localhost:8080/ping/msg", inputValue);
      setResponse(data);
    } catch (error) {
      console.error("Error fetching data: ", error);
      alert("Error fetching data: " + error);
    }
  };

  const handleDeleteData = async () => {
    try {
      const data = await fetchDeleteData("http://localhost:8080/ping/deleteall");
      setResponse(data);
    } catch (error) {
      console.error("Error fetching data: ", error);
      alert("Error fetching data: " + error);
    }
  };

  const handleViewData = async () => {
    try {
      const data = await fetchGetData("http://localhost:8080/ping/getall");
      setResponse(data);
    } catch (error) {
      console.error("Error fetching data: ", error);
      alert("Error fetching data: " + error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Ping Pong</h1>
      <h3>Enter a message:</h3>
      <InputComponent onFetchData={handleFetchData} />
      <h3>Delete all messages:</h3>
      <button onClick={() => handleDeleteData()}>Delete</button>
      <h3>View all messages:</h3>
      <button onClick={() => handleViewData()}>View</button>

      <hr/>
      {response && (
        <div>
          <h3>Response:</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;