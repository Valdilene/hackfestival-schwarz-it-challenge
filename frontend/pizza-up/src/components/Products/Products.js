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
  Button
} from '@mui/material';
import InventoryIcon from '@mui/icons-material/Inventory';

const ItemList = () => {
  const [items, setItems] = useState([]);
  const [today, setToday] = useState('');
  const [upcycleBuffer, setUpcycleBuffer] = useState(0);
  const [filterUpscale, setFilterUpscale] = useState(false);

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
    const todayDate = new Date(today);
    const bufferDate = new Date(todayDate);
    bufferDate.setDate(bufferDate.getDate() + upcycleBuffer);

    if (expiration < todayDate) {
      return '#F44336'; // Calm red background
    } else if (expiration < bufferDate) {
      return '#FFD54F'; // Warm yellow background
    }
    return 'white'; // Default background
  };

  // Filter items based on filterUpscale state
  const filteredItems = filterUpscale
    ? items.filter(item => getBackgroundColor(item.expiresAt) === '#FFD54F')
    : items;

  return (
    <Container maxWidth="lg" style={{ marginTop: '20px' }}>
      <Typography variant="h4" gutterBottom>
        Items List
      </Typography>

      <Grid container spacing={2} style={{ marginBottom: '20px' }}>
        <Grid item xs={12} sm={6} md={3}>
          <TextField
            label="Today"
            type="date"
            fullWidth
            InputLabelProps={{
              shrink: true,
            }}
            value={today}
            onChange={(e) => setToday(e.target.value)}
            InputProps={{
              style: { backgroundColor: 'white' } // Ensure background is white
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <TextField
            label="Upcycle Buffer (days)"
            type="number"
            fullWidth
            value={upcycleBuffer}
            onChange={(e) => setUpcycleBuffer(parseInt(e.target.value, 10) || 0)}
            inputProps={{ min: 0 }}
            InputProps={{
              style: { backgroundColor: 'white' } // Ensure background is white
            }}
          />
        </Grid>
        <Grid item xs={12} sm={12} md={6}>
          <Button
            variant="contained"
            color="primary"
            onClick={() => setFilterUpscale(!filterUpscale)}
          >
            {filterUpscale ? 'Show All' : 'Filter Upscale'}
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={4}>
        {filteredItems.map((item, index) => (
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
