import { useState,useEffect} from "react";
import axios from "axios";


export default function Product(){
      const [product,setProduct]=useState([])
      useEffect(()=>{
            console.log("request to api")
            axios.get("http://127.0.0.1:5000/products")
            .then(response=>setProduct(response.data))
            },[])
            
            const productList=product.map(p=><li>{p.id}{p.name} <img src={p.img}/> {p.price}</li>)
      return(<>
            <ul>
                  <div className="">

                  </div>
                  {productList}      
            </ul>
            </>)
}