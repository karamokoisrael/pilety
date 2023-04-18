import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';


function TabbedNav() {
  return (
    <Tabs
      defaultActiveKey="profile"
      id="uncontrolled-tab-example"
      className="mb-3"
    >
      <Tab eventKey="merch" title="Merch">
      <div>THis is Home</div>
      </Tab>
      <Tab eventKey="mix" title="Mix">
      <div>THis is Profile</div>
      </Tab>
      <Tab eventKey="contact" title="Contact">
        <div>THis is Contact</div>
      </Tab>
    </Tabs>
  );
}

export default TabbedNav;