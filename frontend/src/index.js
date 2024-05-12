import React from 'react';
import App from './components/App';
import "./App.css"
import { createRoot } from 'react-dom/client'

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App  />
  </React.StrictMode>,
  document.getElementById('root')
);