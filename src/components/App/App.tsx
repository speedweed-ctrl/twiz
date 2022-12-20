

import Home from './Home'
import Welcom from 'components/welcomPage/welcom';
import { Routes ,Route } from 'react-router-dom';
function App() {

  

  return (
    <Routes>
      <Route path='/' element={<Welcom/>}/>
      <Route path='/main' element={<Home/>}/>
    </Routes>
  
  );
}

export default App;
