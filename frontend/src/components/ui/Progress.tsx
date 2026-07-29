import React from 'react';

interface ProgressProps {
  value: number; // 0 to 100
  color?: 'purple' | 'cyan' | 'emerald' | 'amber';
  height?: string;
  className?: string;
}

export const Progress: React.FC<ProgressProps> = ({
  value,
  color = 'purple',
  height = 'h-2.5',
  className = ''
}) => {
  const gradientMap = {
    purple: 'bg-gradient-to-r from-purple-600 to-indigo-500',
    cyan: 'bg-gradient-to-r from-cyan-500 to-blue-500',
    emerald: 'bg-gradient-to-r from-emerald-500 to-teal-400',
    amber: 'bg-gradient-to-r from-amber-500 to-orange-500'
  };

  const clamped = Math.min(100, Math.max(0, value));

  return (
    <div className={`w-full bg-slate-800/80 rounded-full overflow-hidden border border-slate-700/50 ${height} ${className}`}>
      <div
        className={`${gradientMap[color]} ${height} rounded-full transition-all duration-500 ease-out`}
        style={{ width: `${clamped}%` }}
      />
    </div>
  );
};
