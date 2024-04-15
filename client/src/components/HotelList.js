import Hotel from './Hotel';
import { useOutletContext } from "react-router-dom";

function HotelList(){

    const {hotels, user} = useOutletContext()

    const hotelComponents = hotels.map(hotel => {
        return <Hotel key={hotel.id} hotel={hotel}/>
    })

    function displayHotelInfo(){
        if(user.type === 'admin'){
            return <h1>Here are all of the hotels:</h1>
        }
        else if(user.type === 'customer' && hotels.length > 0){
            return <h1>Here are the hotels that you've reviewed:</h1>
        }
        else if(user.type === 'customer' && hotels.length === 0){
            return <h1>You haven't reviewed any hotels yet.</h1>
        }
        else{
            return null
        }
    }

    return (
        <>
            <br/>
            {user ? displayHotelInfo() : null}
            <ul className="hotel-list">{hotelComponents}</ul>
        </>
    );
}

export default HotelList;