import React from "react";
import Nav from "../../components/Navbar/navbar";
import Footer from "../../components/Footer/footer";
import Content from "../Content/content";
import "./layout.css";

class Layout extends React.Component {
  render() {
    return (
      <div className="layout">
        <Nav />
        <Content />
        <Content />
        <Content />
        <Content />
        <Footer />
      </div>
    );
  }
}

export default Layout;
