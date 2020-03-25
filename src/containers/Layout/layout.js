import React from "react";
import Nav from "../../components/Navbar/navbar";
import Footer from "../../components/Footer/footer";
import Content from "../Content/content";

class Layout extends React.Component {
  render() {
    return (
      <React.Fragment>
        <Nav />
        <Content />
        <Content />
        <Content />
        <Content />
        <Footer />
      </React.Fragment>
    );
  }
}

export default Layout;
