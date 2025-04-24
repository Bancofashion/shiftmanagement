import { LocationRate, LocationRateCreate } from '../types';
import { api } from './api';

const baseUrl = '/location-rates';
const MAX_RETRIES = 3;
const RETRY_DELAY = 1000; // 1 second

const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

export class LocationRatesApi {
  constructor() {}

  private async retryRequest<T>(fn: () => Promise<T>, retries = MAX_RETRIES): Promise<T> {
    try {
      return await fn();
    } catch (error: any) {
      if (retries > 0 && error.response?.status >= 500) {
        await sleep(RETRY_DELAY);
        return this.retryRequest(fn, retries - 1);
      }
      throw error;
    }
  }

  async getRates(): Promise<LocationRate[]> {
    return this.retryRequest(async () => {
      try {
        const url = `${baseUrl}`;
        console.log('Fetching location rates from:', url);
        const response = await api.get<LocationRate[]>(url, {
          timeout: 10000, // 10 second timeout
          headers: {
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache'
          }
        });
        return response.data;
      } catch (error: any) {
        console.error('Error fetching location rates:', {
          message: error.message,
          status: error.response?.status,
          data: error.response?.data,
          config: error.config
        });
        
        if (error.response?.status === 401) {
          window.location.href = '/login';
          throw new Error('Unauthorized - Please login');
        }
        
        if (error.response?.data?.detail) {
          throw new Error(JSON.stringify(error.response.data.detail));
        }
        throw error;
      }
    });
  }

  async createRate(rate: LocationRateCreate): Promise<LocationRate> {
    return this.retryRequest(async () => {
      try {
        const url = `${baseUrl}`;
        console.log('Creating location rate at:', url);
        const response = await api.post<LocationRate>(url, rate, {
          timeout: 15000, // 15 second timeout for creation
          headers: {
            'Content-Type': 'application/json'
          }
        });
        return response.data;
      } catch (error: any) {
        console.error('Error creating location rate:', {
          message: error.message,
          status: error.response?.status,
          data: error.response?.data,
          config: error.config
        });
        
        if (error.response?.status === 401) {
          window.location.href = '/login';
          throw new Error('Unauthorized - Please login');
        }
        
        if (error.response?.status === 403) {
          throw new Error('Access denied - Admin privileges required');
        }
        
        if (error.response?.status === 400) {
          const errorMessage = error.response.data.detail || 'Invalid rate values';
          throw new Error(errorMessage);
        }
        
        if (error.response?.data?.detail) {
          throw new Error(JSON.stringify(error.response.data.detail));
        }
        throw error;
      }
    });
  }

  async updateRate(id: number, rate: Partial<LocationRateCreate>): Promise<LocationRate> {
    return this.retryRequest(async () => {
      try {
        const url = `${baseUrl}/${id}`;
        console.log('Updating rate at:', url);
        
        const response = await api.put<LocationRate>(url, rate, {
          timeout: 15000,
          headers: {
            'Content-Type': 'application/json'
          }
        });
        return response.data;
      } catch (error: any) {
        console.error('Error updating location rate:', {
          message: error.message,
          status: error.response?.status,
          data: error.response?.data,
          config: error.config,
          url: error.config?.url
        });
        
        if (error.response?.status === 401) {
          window.location.href = '/login';
          throw new Error('Unauthorized - Please login');
        }
        
        if (error.response?.status === 403) {
          throw new Error('Access denied - Admin privileges required');
        }
        
        if (error.response?.status === 400) {
          const errorMessage = error.response.data.detail || 'Invalid rate values';
          throw new Error(errorMessage);
        }
        
        throw error;
      }
    });
  }

  async deleteRate(id: number): Promise<void> {
    return this.retryRequest(async () => {
      try {
        const url = `${baseUrl}/${id}`;
        console.log('Deleting rate at:', url);
        
        await api.delete(url, {
          timeout: 10000,
          headers: {
            'Content-Type': 'application/json'
          }
        });
      } catch (error: any) {
        console.error('Error deleting location rate:', {
          message: error.message,
          status: error.response?.status,
          data: error.response?.data,
          config: error.config,
          url: error.config?.url
        });
        
        if (error.response?.status === 401) {
          window.location.href = '/login';
          throw new Error('Unauthorized - Please login');
        }
        
        if (error.response?.status === 403) {
          throw new Error('Access denied - Admin privileges required');
        }
        
        throw error;
      }
    });
  }
}

// Export a singleton instance
export const locationRatesApi = new LocationRatesApi(); 