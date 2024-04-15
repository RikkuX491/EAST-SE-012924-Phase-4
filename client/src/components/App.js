import Header from "./Header";
import { useState, useEffect } from "react";
import { Outlet, useNavigate, Navigate } from "react-router-dom";
import NavBar from "./NavBar";

function App(){

    const navigate = useNavigate()

    const [hotels, setHotels] = useState([])
    
    const [user, setUser] = useState(null)

    useEffect(() => {
        // GET request - Retrieve all hotels and update the 'hotels' state with the hotel data.
        fetch('/hotels')
        .then(response => response.json())
        .then(hotelsData => setHotels(hotelsData))
    }, [])

    useEffect(() => {
        // GET request - Check if the user is logged in
        fetch('/check_session')
        .then(response => {
            if(response.ok){
                response.json().then(userData => {
                    setUser(userData)
                })
            }
            else if(response.status === 401){
                navigate('/login')
            }
        })
    }, [])

    function addHotel(newHotel){
        // POST request - Create a new hotel and update the 'hotels' state to add the new hotel to the state.
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
        // PATCH request - Update a hotel by id and update the 'hotels' state with the updated hotel data.
        // id - contains a number that refers to the id for the hotel that should be updated.
        // hotelDataForUpdate - contains an object with the hotel data for the PATCH request.
        // setHotelFromHotelsProfile - contains the setter function 'setHotel' from the HotelProfile component.
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
        // DELETE request - Delete a hotel by id and update the 'hotels' state to remove the hotel from the state.
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

    function logInUser(loginData){
        // POST request - Log in a user.
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
                response.json().then(userData => {
                    setUser(userData)
                    navigate('/')
                })
            }
            else if(response.status === 401){
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
        })
    }

    function logOutUser(){
        // DELETE request - Log out a user.
        fetch('/logout', {
            method: "DELETE"
        })
        .then(response => {
            if(response.ok){
                setUser(null)
            }
            else{
                alert("Error: Unable to log user out!")
            }
        })
    }

    return (
      <div className="app">
        <NavBar user={user} logOutUser={logOutUser}/>
        <Header/>
        {user ? <h1>Welcome {user.username}!</h1> : null}
        <Outlet context={{hotels: hotels, addHotel: addHotel, deleteHotel: deleteHotel, updateHotel: updateHotel, logInUser: logInUser}}/>
      </div>
    );
}

export default App;