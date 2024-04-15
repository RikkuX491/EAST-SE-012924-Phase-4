import { NavLink } from "react-router-dom";

function NavBar({customer, logOutUser}){
    return (
        <nav className="navbar">
            {customer ? 
                <>
                    <NavLink to="/">Home</NavLink>
                    <NavLink to="/add_hotel">Add Hotel</NavLink>
                    <NavLink onClick={logOutUser} to="/login">Log Out</NavLink>
                </> 
                :
                <NavLink to="/login">Login</NavLink>
            }
        </nav>
    )
}

export default NavBar;