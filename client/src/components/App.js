import Header from "./Header";
import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import NavBar from "./NavBar";

function App(){

    const [hotels, setHotels] = useState([])

    useEffect(() => {
        // GET request - Write the code to retrieve all hotels and update the 'hotels' state with the hotel data.
    }, [])

    function addHotel(newHotel){
        // POST request - Write the code to create a new hotel and update the 'hotels' state to add the new hotel to the state.
        // newHotel - contains an object with the new hotel data for the POST request.
    }

    function updateHotel(id, hotelDataForUpdate){
        // PATCH request - Write the code to update a hotel by id and update the 'hotels' state with the updated hotel data.
        // id - contains a number that refers to the id for the hotel that should be updated.
        // hotelDataForUpdate - contains an object with the hotel data for the PATCH request.
    }

    function deleteHotel(id){
        // DELETE request - Write the code to delete a hotel by id and update the 'hotels' state to remove the hotel from the state.
        // id - contains a number that refers to the id for the hotel that should be deleted.
    }

    return (
      <div className="app">
        <NavBar/>
        <Header/>
        <Outlet context={{hotels: hotels, addHotel: addHotel, deleteHotel: deleteHotel, updateHotel: updateHotel}}/>
      </div>
    );
}

export default App;