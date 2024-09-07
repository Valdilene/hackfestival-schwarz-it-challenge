import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Grid,
  Card,
  CardContent,
  Typography,
  Container,
  Avatar,
  CardHeader,
} from '@mui/material';
import InventoryIcon from '@mui/icons-material/Inventory';

const ItemList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Fetch data using axios
    axios.get('/api/articles')
      .then(response => {
        const limitedData = response.data.slice(0, 20);
        setItems(limitedData);
      })
      .catch(error => {
        console.error('Error fetching the data', error);
      });
  }, []);

  return (
    <Container maxWidth="lg" style={{ marginTop: '20px' }}>
      <Typography variant="h4" gutterBottom>
        Items List
      </Typography>
      <Grid container spacing={4}>
        {items.map((item, index) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={index}>
            <Card>
              <CardHeader
                avatar={
                  <Avatar>
                    <InventoryIcon />
                  </Avatar>
                }
                title={item.name}
                subheader={`Available: ${item.available}`}
              />
              <CardContent>
                <Typography variant="body2" color="textSecondary">
                  Expiration Date: {new Date(item.expiresAt).toLocaleDateString()}
                </Typography>
                <Typography variant="body2" color="textSecondary">
                  Weight: {item.weight}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default ItemList;
