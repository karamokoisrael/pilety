import React from 'react'
import {Card} from 'react-bootstrap'
import { Link } from 'react-router-dom'
import Table from 'react-bootstrap/Table';

import Rating from './Rating'

function Cargo({cargo}) {
  return (


    <div className="table-responsive">
  <Table striped bordered hover>
    <thead>
      <tr>
        <th>Cargo</th>
        <th>current CBM</th>
        <th>Weight</th>
        <th>date of Depature</th>
        <th>Status</th>
                
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>cargo.name</td>
        <td>cargo.cbm</td>
        <td>cargo.weight</td>
        <td>cargo.depature</td>
        <td>cargo.status</td>
        
         
      </tr>
      
    </tbody>
  </Table>
</div>

  )
}

export default Cargo





