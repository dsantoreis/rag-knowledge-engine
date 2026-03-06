import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { AdminPanel } from '../components/AdminPanel';

describe('AdminPanel', () => {
  it('renders ci gate text', () => {
    render(<AdminPanel />);
    expect(screen.getByText(/CI gate/i)).toBeTruthy();
  });
});
