import React from 'react'

import {Container, Nav, Navbar} from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'


function Header() {
  return (
    <header>    
        <Navbar bg="dark" variant='dark' expand="lg" collapseOnSelect>
          <Container>
            <LinkContainer to={'/'} >
              <Navbar.Brand href="#home">Pilety </Navbar.Brand>
            </LinkContainer>  
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="mr-auto">
                <LinkContainer to={"/products/"}>
                  <Nav.Link><i className='fas fa-shopping-cart'></i> Products</Nav.Link>
                </LinkContainer>
                <LinkContainer to={"/cargo/"}>
                  <Nav.Link><i className='fas fa-user'></i> Cargo</Nav.Link>
                </LinkContainer>
                <LinkContainer to={"/tracking/"}>
                  <Nav.Link><i className='fas fa-user'></i> Tracking</Nav.Link>
                </LinkContainer>
                <LinkContainer to={"/quote/"}>
                  <Nav.Link><i className='fas fa-user'></i> Quote </Nav.Link>
                </LinkContainer>
                <LinkContainer to={"/det/"}>
                  <Nav.Link><i className='fas fa-shopping-cart'></i> Det</Nav.Link>
                </LinkContainer>
                <LinkContainer to={"/login"}>
                  <Nav.Link><i className='fas fa-user'></i> Login</Nav.Link>
                </LinkContainer>
                <LinkContainer to={"/signup"}>
                  <Nav.Link><i className='fas fa-user'></i> Sign Up</Nav.Link>
                </LinkContainer>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>      
    </header>
  )
}

export default Header
