import { create } from 'zustand';
import { DepartmentMetadata, AgentMetadata } from '../types';

interface DashboardState {
  expandedDeptId: string | null;
  selectedAgent: AgentMetadata | null;
  selectedDeptForAgent: DepartmentMetadata | null;
  isDrawerOpen: boolean;
  searchQuery: string;
  categoryFilter: string;
  healthFilter: string;
  agentTypeFilter: string;

  // Actions
  toggleDepartmentExpand: (deptId: string) => void;
  openAgentDrawer: (agent: AgentMetadata, dept?: DepartmentMetadata) => void;
  closeAgentDrawer: () => void;
  setSearchQuery: (query: string) => void;
  setCategoryFilter: (category: string) => void;
  setHealthFilter: (health: string) => void;
  setAgentTypeFilter: (agentType: string) => void;
}

export const useDashboardStore = create<DashboardState>((set) => ({
  expandedDeptId: 'dept_001',
  selectedAgent: null,
  selectedDeptForAgent: null,
  isDrawerOpen: false,
  searchQuery: '',
  categoryFilter: 'ALL',
  healthFilter: 'ALL',
  agentTypeFilter: 'ALL',

  toggleDepartmentExpand: (deptId) =>
    set((state) => ({
      expandedDeptId: state.expandedDeptId === deptId ? null : deptId,
    })),

  openAgentDrawer: (agent, dept) =>
    set({
      selectedAgent: agent,
      selectedDeptForAgent: dept || null,
      isDrawerOpen: true,
    }),

  closeAgentDrawer: () =>
    set({
      isDrawerOpen: false,
    }),

  setSearchQuery: (query) => set({ searchQuery: query }),
  setCategoryFilter: (category) => set({ categoryFilter: category }),
  setHealthFilter: (health) => set({ healthFilter: health }),
  setAgentTypeFilter: (agentType) => set({ agentTypeFilter: agentType }),
}));
