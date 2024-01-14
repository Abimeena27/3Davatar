import React, { useState } from 'react';
import LeftPoster from'./images/LeftPoster.png';
import Header from './Header.jsx'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Home.css'

function Home() {
  const [selectedFile, setSelectedFile] = useState(null);
  
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate('/Result');
  };

  const handleUpload = (e) => {
    setSelectedFile(e.target.files[0]);
    const formData = new FormData();
    formData.append('file', selectedFile);

    axios.post('http://localhost:5000/upload', formData)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error('Error uploading file:', error);
      });
  };

  return (
    <div className='BaseContainer'>
      <Header/>
      <div className="Container">

      <div className='LeftContainer'>
        <img src={LeftPoster} className='LeftImg'></img>
      </div>
      <div className='HomeContainer'>
      <h3 className='HomeText'>Choose the Image File</h3>
      <div className="file-input-wrapper">
        
    <input type="file"   onInput={handleUpload}/>
    
    <label className="custom-file-input">Choose File</label>
</div>
<button onClick={handleButtonClick} className='btn ,ShowBtn'>Show Avatar</button>
     
      </div>
    </div>
    </div>
  );
}

export default Home;
