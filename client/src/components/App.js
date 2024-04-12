import Header from "./Header";
import { useState, useEffect } from "react";
import { Outlet, useNavigate, Navigate } from "react-router-dom";
import NavBar from "./NavBar";

function App(){

    const navigate = useNavigate()

    const [hotels, setHotels] = useState([])
    
    const [customer, setCustomer] = useState(null)

    useEffect(() => {
        // GET request - Write the code to retrieve all hotels and update the 'hotels' state with the hotel data.
        fetch('/hotels')
        .then(response => response.json())
        .then(hotelsData => setHotels(hotelsData))
    }, [])

    useEffect(() => {
        fetch('/check_session')
        .then(response => {
            if(response.ok){
                response.json().then(customerData => {
                    setCustomer(customerData)
                })
            }
            else if(response.status === 401){
                navigate('/login')
            }
        })
    }, [])

    function addHotel(newHotel){
        // POST request - Write the code to create a new hotel and update the 'hotels' state to add the new hotel to the state.
        // newHotel - contains an object with the new hotel data for the POST request.
        fetch('/hotels', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(newHotel)
        })
        .then(response => {
            if(response.ok){
                response.json().then(newHotelData => {
                    setHotels([...hotels, newHotelData])
                    navigate('/')
                })
            }
            else if(response.status === 400){
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
            else{
                response.json().then(() => alert("Error: Something went wrong."))
            }
        })
    }

    function updateHotel(id, hotelDataForUpdate, setHotelFromHotelProfile){
        // PATCH request - Write the code to update a hotel by id and update the 'hotels' state with the updated hotel data.
        // id - contains a number that refers to the id for the hotel that should be updated.
        // hotelDataForUpdate - contains an object with the hotel data for the PATCH request.
        fetch(`/hotels/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(hotelDataForUpdate)
        })
        .then(response => {
            if(response.ok){
                response.json().then(updatedHotelData => {
                    setHotelFromHotelProfile(updatedHotelData)
                    setHotels(hotels => hotels.map(hotel => {
                        if(hotel.id === updatedHotelData.id){
                            return updatedHotelData
                        }
                        else{
                            return hotel
                        }
                    }))
                })
            }
            else if(response.status === 400 || response.status === 404){
                response.json().then(errorData => {
                    alert(`Error: ${errorData.error}`)
                })
            }
            else{
                response.json().then(() => {
                    alert("Error: Something went wrong.")
                })
            }
        })
    }

    function deleteHotel(id){
        // DELETE request - Write the code to delete a hotel by id and update the 'hotels' state to remove the hotel from the state.
        // id - contains a number that refers to the id for the hotel that should be deleted.
        fetch(`/hotels/${id}`, {
            method: "DELETE"
        })
        .then(response => {
            if(response.ok){
                setHotels(hotels => hotels.filter(hotel => {
                    return hotel.id !== id
                }))
            }
            else if(response.status === 404){
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
        })
    }

    function logInCustomer(loginData){
        fetch('/login', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(loginData)
        })
        .then(response => {
            if(response.ok){
                response.json().then(customerData => {
                    setCustomer(customerData)
                    navigate('/')
                })
            }
            else if(response.status === 401){
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
        })
    }

    function logOutCustomer(){
        fetch('/logout', {
            method: "DELETE"
        })
        .then(response => {
            if(response.ok){
                setCustomer(null)
            }
            else{
                alert("Error: Unable to log customer out!")
            }
        })
    }

    return (
      <div className="app">
        <NavBar customer={customer} logOutCustomer={logOutCustomer}/>
        <Header/>
        {customer ? <h1>Welcome {customer.username}!</h1> : null}
        {/* {!customer ? <Navigate to="/login"/> : null} */}
        <Outlet context={{hotels: hotels, addHotel: addHotel, deleteHotel: deleteHotel, updateHotel: updateHotel, logInCustomer: logInCustomer}}/>
      </div>
    );
}

export default App;