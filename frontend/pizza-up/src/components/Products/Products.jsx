import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  List,
  ListItem,
  ListItemText,
  ListItemAvatar,
  Avatar,
  Typography,
  Container,
} from '@mui/material';
import CalendarTodayIcon from '@mui/icons-material/CalendarToday';
import InventoryIcon from '@mui/icons-material/Inventory';
import BalanceIcon from '@mui/icons-material/Balance';

const ItemList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Fetch data using axios
    axios.get('https://your-api-endpoint.com/items')
      .then(response => {
        setItems(response.data);
      })
      .catch(error => {
        console.error('Error fetching the data', error);
      });
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Items List
      </Typography>
      <List>
        {items.map((item, index) => (
          <ListItem key={index}>
            <ListItemAvatar>
              <Avatar>
                <InventoryIcon />
              </Avatar>
            </ListItemAvatar>
            <ListItemText
              primary={item.name}
              secondary={
                <>
                  <Typography component="span" variant="body2" color="textPrimary">
                    Expiration Date: 
                  </Typography> {new Date(item.expirationDate).toLocaleDateString()} <br />
                  <Typography component="span" variant="body2" color="textPrimary">
                    Available: 
                  </Typography> {item.available} units <br />
                  <Typography component="span" variant="body2" color="textPrimary">
                    Weight: 
                  </Typography> {item.weight}
                </>
              }
            />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default ItemList;
