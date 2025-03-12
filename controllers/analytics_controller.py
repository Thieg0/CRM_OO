from models.report import Report

class AnalyticsController:
    """
    Controller for managing operations related to reports and analytics.
    """
    
    def __init__(self, view, analytics_repository, contact_repository, sales_pipeline_repository, lead_repository):
        """
        Initializes the controller with view and repositories.
        
        Args:
            view: AnalyticsView object for user interaction.
            analytics_repository: Repository to store reports.
            contact_repository: Repository for contact data.
            sales_pipeline_repository: Repository for sales data.
            lead_repository: Repository for lead data.
        """
        self.view = view
        self.repository = analytics_repository
        self.contact_repository = contact_repository
        self.sales_pipeline_repository = sales_pipeline_repository
        self.lead_repository = lead_repository
    
    def generate_sales_report(self):
        """
        Generates a sales performance report.
        """
        opportunities = self.sales_pipeline_repository.get_all()
        
        # Calculate report data
        data = {
            'total_opportunities': len(opportunities),
            'by_stage': self._get_opportunities_by_stage(opportunities),
            'total_value': self._calculate_total_value(opportunities),
            'conversion_rate': self._calculate_conversion_rate(opportunities)
        }
        
        # Create and store the report
        report = Report("Sales Performance Report", "sales", data)
        self.repository.add(report)
        
        return report
    
    def generate_lead_report(self):
        """
        Generates a lead analysis report.
        """
        leads = self.lead_repository.get_all()
        opportunities = self.sales_pipeline_repository.get_all()
        
        # Calculate report data
        data = {
            'total_leads': len(leads),
            'by_status': self._get_leads_by_status(leads),
            'by_source': self._get_leads_by_source(leads),
            'conversion_funnel': self._get_conversion_funnel(leads, opportunities)
        }
        
        # Create and store the report
        report = Report("Lead Analysis Report", "leads", data)
        self.repository.add(report)
        
        return report
    
    def generate_pipeline_report(self):
        """
        Generates a pipeline analysis report.
        """
        opportunities = self.sales_pipeline_repository.get_all()
        
        # Calculate report data
        data = {
            'stage_distribution': self._get_opportunities_by_stage(opportunities),
            'value_by_stage': self._get_value_by_stage(opportunities),
            'average_deal_size': self._calculate_average_deal_size(opportunities)
        }
        
        # Create and store the report
        report = Report("Pipeline Analysis Report", "pipeline", data)
        self.repository.add(report)
        
        return report
    
    def list_reports(self):
        """
        Lists all generated reports.
        """
        reports = self.repository.get_all()
        self.view.show_reports(reports)
    
    def view_report(self):
        """
        Views a specific report in detail.
        """
        reports = self.repository.get_all()
        
        if not reports:
            self.view.show_message("No reports generated yet.")
            return
            
        self.view.show_reports(reports)
        index = self.view.get_report_index(len(reports))
        
        if index is not None:
            report = self.repository.get(index)
            self.view.show_report(report)
    
    # Helper methods for report generation
    def _get_opportunities_by_stage(self, opportunities):
        """
        Counts opportunities by stage.
        
        Args:
            opportunities (list): List of opportunity objects.
            
        Returns:
            dict: Counts of opportunities by stage.
        """
        stages = {}
        for opp in opportunities:
            stages[opp.stage] = stages.get(opp.stage, 0) + 1
        return stages
    
    def _calculate_total_value(self, opportunities):
        """
        Calculates the total value of all opportunities.
        
        Args:
            opportunities (list): List of opportunity objects.
            
        Returns:
            float: Total value.
        """
        return sum(opp.value for opp in opportunities)
    
    def _calculate_conversion_rate(self, opportunities):
        """
        Calculates the conversion rate of opportunities.
        
        Args:
            opportunities (list): List of opportunity objects.
            
        Returns:
            float: Conversion rate percentage.
        """
        if not opportunities:
            return 0
            
        closed_won = sum(1 for opp in opportunities if opp.stage == "Closed")
        total = len(opportunities)
        return (closed_won / total * 100) if total > 0 else 0
    
    def _get_leads_by_status(self, leads):
        """
        Counts leads by status.
        
        Args:
            leads (list): List of lead objects.
            
        Returns:
            dict: Counts of leads by status.
        """
        status_count = {}
        for lead in leads:
            status_count[lead.status] = status_count.get(lead.status, 0) + 1
        return status_count
    
    def _get_leads_by_source(self, leads):
        """
        Counts leads by source.
        
        Args:
            leads (list): List of lead objects.
            
        Returns:
            dict: Counts of leads by source.
        """
        source_count = {}
        for lead in leads:
            source_count[lead.source] = source_count.get(lead.source, 0) + 1
        return source_count
    
    def _get_conversion_funnel(self, leads, opportunities):
        """
        Calculates conversion funnel metrics.
        
        Args:
            leads (list): List of lead objects.
            opportunities (list): List of opportunity objects.
            
        Returns:
            dict: Conversion funnel metrics.
        """
        qualified_leads = sum(1 for lead in leads if lead.status == "Qualified")
        closed_deals = sum(1 for opp in opportunities if opp.stage == "Closed")
        
        return {
            'total_leads': len(leads),
            'qualified_leads': qualified_leads,
            'opportunities': len(opportunities),
            'closed_deals': closed_deals
        }
    
    def _get_value_by_stage(self, opportunities):
        """
        Calculates the total value of opportunities by stage.
        
        Args:
            opportunities (list): List of opportunity objects.
            
        Returns:
            dict: Total value by stage.
        """
        value_by_stage = {}
        for opp in opportunities:
            value_by_stage[opp.stage] = value_by_stage.get(opp.stage, 0) + opp.value
        return value_by_stage
    
    def _calculate_average_deal_size(self, opportunities):
        """
        Calculates the average deal size.
        
        Args:
            opportunities (list): List of opportunity objects.
            
        Returns:
            float: Average deal size.
        """
        total_value = self._calculate_total_value(opportunities)
        total_deals = len(opportunities)
        return total_value / total_deals if total_deals > 0 else 0