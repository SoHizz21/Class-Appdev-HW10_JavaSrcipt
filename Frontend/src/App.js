import {BrowserRouter,Route,Routes,Link} from "react-router-dom";
import Product from "./product";
export default function App() {
  return (
   
    // <BrowserRouter>
    //   <Link to="/products">About</Link>
    //   <Link to="/poet">About</Link>
    //   <Link to="about">About</Link>

    //   <Routes>
    //     <Route path="/products" element={<Product/>}/>
    //   </Routes>
    // </BrowserRouter>
   
    <Product/>
  );
}


