import { NavLink } from "react-router-dom";

function NavBar({user, logOutUser}){
    return (
        <nav className="navbar">
            {/* {user ? 
                <>
                    <NavLink to="/">Home</NavLink>
                    <NavLink to="/add_hotel">Add Hotel</NavLink>
                    <NavLink onClick={logOutUser} to="/login">Log Out</NavLink>
                </> 
                :
                <NavLink to="/login">Login</NavLink>
            } */}
            {user ? <NavLink to="/">Home</NavLink> : null}
            {user && user.type === 'admin' ? <NavLink to="/add_hotel">Add Hotel</NavLink> : null}
            {user ? <NavLink onClick={logOutUser} to="/login">Log Out</NavLink> : null}
            {!user ? <NavLink to="/login">Login</NavLink> : null}
            {!user ? <NavLink to="/signup">Signup</NavLink> : null}
        </nav>
    )
}

export default NavBar;