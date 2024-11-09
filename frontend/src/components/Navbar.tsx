import { useState } from 'react';
import { Link } from 'react-router-dom';




const Navbar = () => {

        const [isOpen, setIsOpen] = useState(false);
    
        const toggleDropdown = () => {
            setIsOpen(!isOpen);
        };
        const closeDropdown = () => {
            setIsOpen(false);
        };

    return (
        <>
            <nav className="navbar bg-base-100">
                <div className="navbar-start">
                    <div className="dropdown lg:hidden">
                        <div tabIndex={0} role='button' className="btn btn-ghost btn-circle" onClick={toggleDropdown}>
                            <span className="material-symbols-outlined">
                                menu 
                            </span>
                        </div>
                        {isOpen && (
                            <ul tabIndex={0} className="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                                <li><Link to="/winter" onClick={closeDropdown} className=""> Winter </Link></li>
                                <li><Link to="/summer" onClick={closeDropdown}  className=""> Summer </Link></li>
                            </ul>
                        )}
                    </div>
                    <Link to="/" className="text-xl font-extrabold px-4">Feeble</Link>
                </div>
                <div className="navbar-end gap-4">
                    <div className="hidden lg:flex lg:gap-3">
                        <Link to="/winter" className=""> Winter </Link>
                        <Link to="/summer" className=""> Summer </Link>
                    </div>
                    <Link to="/login" className="btn">Log in</Link>
                    <Link to="/cart" className="btn btn-secondary">
                        <span className="material-symbols-outlined">
                            shopping_cart
                        </span>
                    </Link>
                </div>

            </nav>
        </>
    )
}

export default Navbar;