import React from 'react';
import 'aframe';
import Avatar from "./images/output_model.glb";

const AframeScene = () => {
  return (
    <a-scene>
      <a-entity gltf-model={Avatar} position="0 1 -3" rotation="0 90 0" scale="0.5 0.5 0.5" id="Avatar"></a-entity>

      <a-camera position="0 1.1 0"></a-camera>
      <a-light type="ambient" color="#888"></a-light>
      <a-light type="directional" position="-5 5 5" target="#Avatar"></a-light> 

      <a-plane rotation="-90 0 0" width="20" height="20" color="#7BC8A4"></a-plane>
    </a-scene>
  );
};

export default AframeScene;
