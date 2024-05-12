import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";

const Navbar = () => {
    return (
        <>
            <Nav>
                <NavMenu>
                    <NavLink to="/" activeStyle>
                        Home
                    </NavLink>
                    <NavLink to="/meal_request" activeStyle>
                        Meal Request
                    </NavLink>
                    <NavLink to="/ingredient_request" activeStyle>
                        Ingredient Request
                    </NavLink>
                    <NavLink to="/vote" activeStyle>
                        Vote
                    </NavLink>
                    <NavLink to="/schedule_change" activeStyle>
                        Schedule Change
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;