import {BrowserRouter,Route,Routes,Link} from "react-router-dom";
import Product from "./product";

export default function App() {
  return (
    <form style={{textAlign: "center"}}>
      <BrowserRouter>
      <div style={{textAlign: "center"}}>
      <h1>GET</h1>
        <Link to="/products">
        <input type="submit"/>
        </Link>
        <br/>
      </div>
      
      <Routes>
        <Route path="/products" element={<Product/>}/>
      </Routes>
     </BrowserRouter> 
    
      
      <h1>POST</h1>
      <label>
        id:
        <input type="text" _id="id" /><br/>
        Name:
        <input type="text" name="Name" /><br/>
        Price:
        <input type="text" id="Price" /><br/>
        imgLink:
        <input type="text" id="img" /><br/>
      </label>
      <input type="submit"/>

      <br/><br/>
      
      <h1>Update</h1>
      <label>
        id:
        <input type="text" _id="id" />
      </label>
      <input type="submit"/>
      <br/><br/>

      <h1>delete</h1>
      <label>
        id:
        <input type="text" _id="id" />
      </label>
      <input type="submit"/>
      <br/><br/>
     
    </form>

  );
}


