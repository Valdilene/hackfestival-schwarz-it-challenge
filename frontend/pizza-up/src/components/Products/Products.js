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
  TextField,
} from '@mui/material';
import InventoryIcon from '@mui/icons-material/Inventory';

const ItemList = () => {
  const [items, setItems] = useState([]);
  const [upcycledDate, setUpcycledDate] = useState('');
  const [expireDate, setExpireDate] = useState('');

  useEffect(() => {
    // Fetch data using axios
    axios.get('/api/articles')
      .then(response => {
        // Limit the data to the first 20 items
        const limitedData = response.data.slice(0, 20);
        setItems(limitedData);
      })
      .catch(error => {
        console.error('Error fetching the data', error);
      });
  }, []);

  // Helper function to get the background color based on dates
  const getBackgroundColor = (expiresAt) => {
    const expiration = new Date(expiresAt);
    const upcycled = new Date(upcycledDate);
    const expire = new Date(expireDate);

    if (expiration >= upcycled && expiration <= expire) {
      return '#FFD54F'; // Warm yellow background
    } else if (expiration > expire) {
      return '#F44336'; // Calm red background
    }
    return 'white'; // Default background
  };


  return (
    <Container maxWidth="lg" style={{ marginTop: '20px' }}>
      <Typography variant="h4" gutterBottom>
        Items List
      </Typography>

      <Grid container spacing={2} style={{ marginBottom: '20px' }}>
        <Grid item xs={12} sm={6} md={3}>
          <TextField
            label="Upcycled Date"
            type="date"
            fullWidth
            InputLabelProps={{
              shrink: true,
            }}
            value={upcycledDate}
            onChange={(e) => setUpcycledDate(e.target.value)}
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <TextField
            label="Expire Date"
            type="date"
            fullWidth
            InputLabelProps={{
              shrink: true,
            }}
            value={expireDate}
            onChange={(e) => setExpireDate(e.target.value)}
          />
        </Grid>
      </Grid>

      <Grid container spacing={4}>
        {items.map((item, index) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={index}>
            <Card style={{
              backgroundColor: getBackgroundColor(item.expiresAt),
              color: getBackgroundColor(item.expiresAt) === '#F44336' ? 'white' : 'black'
            }}>
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
